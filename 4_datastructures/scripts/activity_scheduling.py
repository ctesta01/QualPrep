def greedy_movie_scheduler(movies):
    """
    Select the maximum number of non-overlapping movies.

    Args:
    movies (list of tuples): Each tuple contains two integers (start, finish)
                             representing the start and finish times of a movie.

    Returns:
    list: A list of selected movies in the format (start, finish).
    """
    # Sort movies by their finishing times
    sorted_movies = sorted(movies, key=lambda x: x[1])

    # List to store selected movies
    selected_movies = []

    # The time at which the last selected movie finishes
    last_finish_time = 0

    # Iterate through the sorted list of movies
    for start, finish in sorted_movies:
        # If the movie starts after or when the last selected movie finishes
        if start >= last_finish_time:
            # Select the movie
            selected_movies.append((start, finish))
            # Update the finish time to the finish time of the currently selected movie
            last_finish_time = finish

    return selected_movies

# Example list of movies as (start time, end time)
movies = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10), (9, 11), (11, 14), (13, 16)]

# Get the list of selected movies
selected_movies = greedy_movie_scheduler(movies)

print("Selected movies:", selected_movies)