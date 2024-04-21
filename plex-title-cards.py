import yaml
import argparse
from plexapi.server import PlexServer

def upload_poters(yaml_file, plex_url, token):
    plex = PlexServer(plex_url, token)

    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    for library_name, library_data in data.items(): 
        try:
            library = plex.library.section(library_name)
        except:
            print(f"No Library found with name '{library_name}'")
            continue

        print(f"Adding to Library '{library_name}'")
            
        for tvdb_id, data in library_data.items():
            try:
                show = library.getGuid(f"tvdb://{tvdb_id}")
            except:
                print(f"No TV show found with TVDB ID '{tvdb_id}'. Skipping")
                continue

            if 'url_poster' in data:
                show.uploadPoster(data['url_poster'])
                print(f"Poster uploaded successfully for '{show.title}'")
            if 'url_background' in data:
                show.uploadArt(data['url_background'])
                print(f"Background uploaded successfully for '{show.title}'")

            # Assume if there are no numbered seasons that the provided season is the first season
            seasons_data = data.get('seasons')
            if sum(isinstance(key, int) for key in seasons_data.keys()) == 0:
                seasons_data[1] = seasons_data

            # Update season posters
            for season_num, season_data in seasons_data.items():
                try:
                    season = show.season(season_num)
                except:
                    print(f"Season {season_num} not found for '{show.title}'")
                    continue

                if 'url_poster' in season_data:
                    season.uploadPoster(season_data['url_poster'])
                    print(f"Poster uploaded successfully for season {season_num} of '{show.title}'")

                # Update episode posters
                for episode_num, episode_data in season_data.get('episodes', {}).items():
                    try:
                        episode = season.episode(episode_num)
                    except:
                        print(f"No episode found for S{season_num}E{episode_num} of '{show.title}'")
                        continue

                    if 'url_poster' in episode_data:
                        episode.uploadPoster(episode_data['url_poster'])
                        print(f"Poster uploaded successfully for S{season_num}E{episode_num} of '{show.title}'")

# Example usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Update your Plex server with MediUX Cards!")
    parser.add_argument('file', metavar='FILE', type=str, help='input file to process')
    parser.add_argument('-c', '--config', type=str, default='config.yaml', help='optional config file (default: config.yaml)')
    
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config_data = yaml.safe_load(f)

    upload_poters(args.file, config_data['plex_url'], config_data['token'])
