# Lumber Futures
This is a web application that visualizes the prices of lumber futures over time. The server is written in Python/Django and the client is in TypeScript/React.

## To run
1. First, clone the project: `git clone https://github.com/ecoates.bc/lumber_futures`
2. The required dependencies are `python`, `pip`, `node`, and `npm`.
3. Navigate to `lumber_futures/server` and run `pip install -r requirements.txt` and `python3 manage.py migrate`
4. Load the data by running `python3 manage.py load_plot_data --file ../lumberFut.xlsx`
5. Start the server by running `python3 manage.py runserver`
6. In a new terminal, navigate to `lumber_futures/client`
7. Start the client by running `npm start`