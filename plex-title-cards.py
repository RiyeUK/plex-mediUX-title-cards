import yaml
import pprint
import argparse
from plexapi.server import PlexServer

def upload_posters(yaml_file, plex_url, token):
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
            
        for id, data in library_data.items():
            if "seasons" in data:
                upload_show(id, data, library)
            else:
                upload_movie(id, data, library)

def upload_show(tvdb_id, show_data, library):
    try:
        show = library.getGuid(f"tvdb://{tvdb_id}")
    except:
        print(f"Unable to find show with TVDB ID of {tvdb_id}")
        return

    if 'url_poster' in show_data:
        show.uploadPoster(show_data['url_poster'])
        print(f"Poster uploaded successfully for '{show.title}'")
    if 'url_background' in show_data:
        show.uploadArt(show_data['url_background'])
        print(f"Background uploaded successfully for '{show.title}'")

    # Assume if there are no numbered seasons that the provided season is the first season
    seasons_data = show_data.get('seasons')
    if sum(isinstance(key, int) for key in seasons_data.keys()) == 0:
        seasons_data[1] = seasons_data

    for season_number, season_data in seasons_data.items():
        upload_season(show, season_number, season_data)

def upload_season(show, season_number, season_data):
    try:
        season = show.season(season_number)
    except:
        print(f"Season {season_number} not found for '{show.title}'")
        return

    if 'url_poster' in season_data:
        season.uploadPoster(season_data['url_poster'])
        print(f"Poster uploaded successfully for season {season_number} of '{show.title}'")

    # Update episode posters
    for episode_number, episode_data in season_data.get('episodes', {}).items():
        try:
            episode = season.episode(episode_number)
        except:
            print(f"No episode found for S{season_number}E{episode_number} of '{show.title}'")
            continue

        if 'url_poster' in episode_data:
            episode.uploadPoster(episode_data['url_poster'])
            print(f"Poster uploaded successfully for S{season_number}E{episode_number} of '{show.title}'")
    
def upload_movie(tmdb_id, movie_data, library):
    try:
        movie = library.getGuid(f"tmdb://{tmdb_id}")
    except:
        print(f"Unable to find Movie with tmdb id of {tmdb_id}")
        return

    if 'url_poster' in movie_data:
        movie.uploadPoster(movie_data['url_poster'])
        print(f"Poster uploaded successfully for '{movie.title}'")
    if 'url_background' in movie_data:
        movie.uploadArt(movie_data['url_background'])
        print(f"Background uploaded successfully for '{movie.title}'")
# Example usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Update your Plex server with MediUX Cards!")
    parser.add_argument('file', metavar='FILE', type=str, help='input file to process')
    parser.add_argument('-c', '--config', type=str, default='config.yaml', help='optional config file (default: config.yaml)')
    
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config_data = yaml.safe_load(f)

    upload_posters(args.file, config_data['plex_url'], config_data['token'])
