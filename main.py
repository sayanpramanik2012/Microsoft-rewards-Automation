# main.py

from ui import Application
from data_handler import delete_search_data_file
import atexit

def main():
    atexit.register(delete_search_data_file)
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
