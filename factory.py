class Database:
  """
  This class implements the Singleton pattern to ensure only one
  database connection instance exists throughout the program.
  """

  _instance = None  # Private attribute to store the singleton instance

  def __new__(cls):
    """
    The __new__ method is used to control object creation.
    It prevents direct instantiation using the `Database()` call.
    """
    if not cls._instance:
      cls._instance = super().__new__(cls)  # Call superclass for actual creation
    return cls._instance

  def __init__(self):
    # Initialization code for the database connection (replace with actual logic)
    # ...
    pass

  @staticmethod
  def get_instance():
    """
    Static method to access the singleton instance.
    """
    return Database._instance

  def query(self, sql):
    # Execute the SQL query on the database connection (replace with actual logic)
    # ...
    pass

# Example usage in another class
class Application:
  def main(self):
    # Get the database instance
    db = Database.get_instance()

    # Use the database for queries
    db.query("SELECT ...")
    # ...

    # Another variable will reference the same instance
    db2 = Database.get_instance()
    db2.query("SELECT ...")
    # ...
