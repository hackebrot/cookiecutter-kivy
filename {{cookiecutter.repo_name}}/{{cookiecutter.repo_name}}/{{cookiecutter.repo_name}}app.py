from kivy.app import App


class {{ cookiecutter.repo_name|capitalize }}App(App):
    """Basic kivy app

    Edit {{ cookiecutter.repo_name }}.kv to get started.
    """

    def build(self):
        return self.root

