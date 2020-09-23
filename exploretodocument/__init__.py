from .exploretodocument import Exploretodocument

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = Exploretodocument(parent=app)
app.addExtension(extension)
