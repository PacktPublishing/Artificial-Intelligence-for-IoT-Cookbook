
var todoDB = (function() {
  var tDB = {};
  var datastore = null;

  /**
   * Open a connection to the datastore.
   */
  tDB.open = function(callback) {
    // Database version.
    var version = 1;

    // Open a connection to the datastore.
    var request = indexedDB.open('todos', version);

    // Handle datastore upgrades.
    request.onupgradeneeded = function(e) {
      var db = e.target.result;

      e.target.transaction.onerror = tDB.onerror;

      // Delete the old datastore.
      if (db.objectStoreNames.contains('todo')) {
        db.deleteObjectStore('todo');
      }

      // Create a new datastore.
      var store = db.createObjectStore('todo', {
        keyPath: 'timestamp'
      });
    };

    // Handle successful datastore access.
    request.onsuccess = function(e) {
      // Get a reference to the DB.
      datastore = e.target.result;
      
      // Execute the callback.
      callback();
    };

    // Handle errors when opening the datastore.
    request.onerror = tDB.onerror;
  };


  /**
   * Fetch all of the todo items in the datastore.
   * @param {function} callback A function that will be executed once the items
   *                            have been retrieved. Will be passed a param with
   *                            an array of the todo items.
   */
  tDB.fetchTodos = function(callback) {
    var db = datastore;
    var transaction = db.transaction(['todo'], 'readwrite');
    var objStore = transaction.objectStore('todo');

    var keyRange = IDBKeyRange.lowerBound(0);
    var cursorRequest = objStore.openCursor(keyRange);

    var todos = [];

    transaction.oncomplete = function(e) {
      // Execute the callback function.
      callback(todos);
    };

    cursorRequest.onsuccess = function(e) {
      var result = e.target.result;
      
      if (!!result == false) {
        return;
      }
      
      todos.push(result.value);

      result.continue();
    };

    cursorRequest.onerror = tDB.onerror;
  };


  /**
   * Create a new todo item.
   * @param {string} text The todo item.
   */
  tDB.createTodo = function(text, callback) {
    // Get a reference to the db.
    var db = datastore;

    // Initiate a new transaction.
    var transaction = db.transaction(['todo'], 'readwrite');

    // Get the datastore.
    var objStore = transaction.objectStore('todo');

    // Create a timestamp for the todo item.
    var timestamp = new Date().getTime();
    
    // Create an object for the todo item.
    var todo = {
      'text': text,
      'timestamp': timestamp
    };

    // Create the datastore request.
    var request = objStore.put(todo);

    // Handle a successful datastore put.
    request.onsuccess = function(e) {
      // Execute the callback function.
      callback(todo);
    };

    // Handle errors.
    request.onerror = tDB.onerror;
  };


  /**
   * Delete a todo item.
   * @param {int} id The timestamp (id) of the todo item to be deleted.
   * @param {function} callback A callback function that will be executed if the 
   *                            delete is successful.
   */
  tDB.deleteTodo = function(id, callback) {
    var db = datastore;
    var transaction = db.transaction(['todo'], 'readwrite');
    var objStore = transaction.objectStore('todo');
    
    var request = objStore.delete(id);
    
    request.onsuccess = function(e) {
      callback();
    }
    
    request.onerror = function(e) {
      console.log(e);
    }
  };


  // Export the tDB object.
  return tDB;
}());
