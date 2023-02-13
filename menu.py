import wezel
#from action import HelloWorld

#def hello_world(parent):
 # """Define a function to create HelloWorld button.
  
  #Creates an example 'HelloWorld' button based on the
  #action defined in action.py
  #"""
  #parent.action(HelloWorld, text='HelloWorld')


def default(parent):
  """Create default menubar.
  
  Builds default wezel menubar as shown in
  wezel package.
  """
  wezel.menu.folder.all(parent.menu('File'))
  wezel.menu.edit.all(parent.menu('Edit'))
  wezel.menu.view.all(parent.menu('View'))
  wezel.menu.filter.all(parent.menu('Filter'))
  wezel.menu.segment.all(parent.menu('Segment'))
  wezel.menu.transform.all(parent.menu('Transform'))
  wezel.menu.about.all(parent.menu('About'))


#def custom(parent):
 # """Create custom menubar.
  
  #Builds default wezel menubar with addition of
  #'HelloWorld' button defined in 'hello_world'
  #function above.
  #"""
  #wezel.menu.folder.all(parent.menu('File'))
  #wezel.menu.edit.all(parent.menu('Edit'))
  #wezel.menu.view.all(parent.menu('View'))
  #wezel.menu.filter.all(parent.menu('Filter'))
  #wezel.menu.segment.all(parent.menu('Segment'))
  #wezel.menu.transform.all(parent.menu('Transform'))
  #wezel.menu.about.all(parent.menu('About'))
  #hello_world(parent.menu('HelloWorld'))
