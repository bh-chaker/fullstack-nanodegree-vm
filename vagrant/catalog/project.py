from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, make_response
app = Flask(__name__)

from flask import session as login_session

import json

from authentication_utils import init_csrf_token, check_csrf_token, gconnect, gdisconnect
from database_utils import getCategories, getCategory, getItems, getItem, addItem, updateItem, removeItem

@app.before_request
def before_request():
  """This function is run before each request.
  It initializes and checks CSRF token."""
  if request.method == 'GET' and request.endpoint != 'static':
    init_csrf_token( login_session )
  elif request.method == 'POST' and not check_csrf_token( login_session, request ):
    response = make_response(json.dumps({'success': False, 'message': 'Invalid csrf_token parameter.'}), 401)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/catalog/<category_name>/JSON/')
def categoryJSON(category_name):
  """JSON endpoint to view Category information"""
  items = getItems(category_name)
  return jsonify(Items=[i.serialize for i in items])


@app.route('/catalog/<category_name>/item/<item_name>/JSON/')
def itemJSON(category_name, item_name):
  """JSON endpoint to view Item information"""
  item = getItem(category_name, item_name)
  return jsonify(item = item.serialize)

@app.route('/catalog/JSON/')
def categorieJSON():
  """JSON endpoint to view All Categories information"""
  categories = getCategories()
  return jsonify(categories = [r.serialize for r in categories])

@app.route('/')
@app.route('/catalog/')
def showCatalog():
  """Show list of Categories. This is home page."""
  categories = getCategories()
  return render_template('catalog.html', categories = categories)

@app.route('/catalog/<category_name>/')
def showCategory(category_name):
  """Show list of Items of a Category"""
  category = getCategory(category_name)
  items = getItems(category_name)
  return render_template('category.html', items = items, category = category)

@app.route('/catalog/<category_name>/new/', methods=['GET','POST'])
def newItem(category_name):
  """Add new item"""

  #Only logged in users allowed to view this page
  if 'username' not in login_session:
    return redirect(url_for('showCatalog'))

  categories = getCategories()

  if request.method == 'POST':
    #If the form has been submitted, try to add a new user
    category = getCategory(request.form['category_name'])
    item_data = {
      'name' : request.form['name'],
      'description': request.form['description'],
      'image_url': request.form['image_url'],
      'category_id': category.id,
      'user_id': login_session['user_id'],
      }
    if addItem(item_data):
      flash('New %s Item Successfully Created' % (request.form['name']), 'success')
      return redirect(url_for('showCategory', category_name = request.form['category_name']))
    else:
      flash('The name %s is already used in this category!' % (request.form['name']), 'danger')
      return render_template('itemForm.html', categories = categories, category = category)

  else:
    #Display the form in case of GET request
    category = getCategory(category_name)
    return render_template('itemForm.html', categories = categories, category = category)

@app.route('/catalog/<category_name>/item/<item_name>/', methods=['GET'])
def showItem(category_name, item_name):
  """Show an Item"""
  item = getItem(category_name, item_name)
  category = getCategory(category_name)
  return render_template('item.html', category = category, item = item)

#Edit an item
@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET','POST'])
def editItem(category_name, item_name):
  """Edit an item"""

  #Only logged in users allowed to view this page
  if 'username' not in login_session:
    return redirect(url_for('showCatalog'))


  item = getItem(category_name, item_name)
  category = getCategory(category_name)

  if request.method == 'POST':
    #If the form has been submitted, try to edit the Item
    if updateItem(item, request.form):
      flash('Item Successfully Edited', 'success')
      return redirect(url_for('showCategory', category_name = category_name))
    else:
      flash('Item Was Not Edited', 'danger')
      return redirect(url_for('editItem', category_name = category_name, item_name=item_name))
  else:
    #Display the form in case of GET request
    return render_template('itemForm.html', categories = getCategories(), category = category, item_name = item_name, item = item)

@app.route('/catalog/<category_name>/item/<item_name>/delete', methods = ['GET','POST'])
def deleteItem(category_name,item_name):
  """Delete an Item"""

  #Only logged in users allowed to view this page
  if 'username' not in login_session:
    return redirect(url_for('showCatalog'))

  category = getCategory(category_name)
  itemToDelete = getItem(category_name, item_name)

  if request.method == 'POST':
    #If the form has been submitted, delete the Item
    removeItem(itemToDelete)
    flash('Item Successfully Deleted', 'success')
    return redirect(url_for('showCategory', category_name = category_name))
  else:
    #Display the form in case of GET request
    return render_template('deleteItem.html', category = category, item = itemToDelete)


@app.route('/connect', methods=['POST'])
def connect():
  """Processes third party authentication service response."""

  #Currently, only Google is supported
  if request.form['provider'] == 'google':
    #Call gconnect function from authentication_utils module
    message, http_code = gconnect(login_session, request)
    success = http_code==200
    response = make_response(json.dumps({'success': success, 'message': message}, http_code))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/disconnect')
def disconnect():
  """Disconnect user based on provider"""

  if 'provider' in login_session:
    #Currently, only Google is supported
    if login_session['provider'] == 'google':
      success = gdisconnect(login_session)

    if success:
      flash("You have successfully been logged out.", 'success')
    else:
      flash("Could not log you out.", 'danger')

    return redirect(url_for('showCatalog'))
  else:
    flash("You were not logged in", 'warning')
    return redirect(url_for('showCatalog'))

#Start the server on port 8000
if __name__ == '__main__':
  app.secret_key = 'YjVPtCcf59uphMUPXZEPqsXdcxbEXDyq'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)
