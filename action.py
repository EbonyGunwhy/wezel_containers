import wezel

class HelloWorld(wezel.gui.Action):

  def run(self, app):
    app.dialog.information('HelloWorld')
