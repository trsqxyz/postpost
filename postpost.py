import toga

class Postpost(toga.App):
    def username(self):
        return 'WRITE YOUR NAME HERE.'

    def startup(self):
        self.urls = {
                'login': 'http://prgrphs.tokyo/auth/twitter',
                'home': 'http://prgrphs.tokyo/{0}'.format(self.username()),
                'new': 'http://prgrphs.tokyo/{0}/new'.format(self.username()),
                'logout': 'http://prgrphs.tokyo/logout',
        }

        container = toga.Container()

        self.webview = toga.WebView()
        self.webview.url = 'http://prgrphs.tokyo/'

        login_btn = toga.Button('login', on_press=self.login_page)
        home_btn = toga.Button('home', on_press=self.home_page)
        new_btn = toga.Button('new', on_press=self.new_page)
        logout_btn = toga.Button('logout', on_press=self.logout_page)

        container.add(self.webview)
        container.add(login_btn)
        container.add(home_btn)
        container.add(new_btn)
        container.add(logout_btn)

        container.constrain(self.webview.TOP == container.TOP)
        container.constrain(self.webview.LEFT == container.LEFT)
        container.constrain(self.webview.RIGHT == container.RIGHT)

        container.constrain(login_btn.TOP == self.webview.BOTTOM)
        container.constrain(login_btn.LEFT == container.LEFT)
        container.constrain(login_btn.RIGHT == home_btn.LEFT)
        container.constrain(login_btn.BOTTOM == container.BOTTOM)

        container.constrain(home_btn.TOP == self.webview.BOTTOM)
        container.constrain(home_btn.RIGHT == new_btn.LEFT)
        container.constrain(home_btn.BOTTOM == container.BOTTOM)

        container.constrain(new_btn.TOP == self.webview.BOTTOM)
        container.constrain(new_btn.RIGHT == logout_btn.LEFT)
        container.constrain(new_btn.BOTTOM == container.BOTTOM)

        container.constrain(logout_btn.TOP == self.webview.BOTTOM)
        container.constrain(logout_btn.RIGHT == self.webview.RIGHT)
        container.constrain(logout_btn.BOTTOM == container.BOTTOM)

        app.main_window.content = container

    def login_page(self, widget):
        self.webview.url =  self.urls['login']

    def home_page(self, widget):
        self.webview.url = self.urls['home']

    def new_page(self, widget):
        self.webview.url = self.urls['new']

    def logout_page(self, widget):
        self.webview.url = self.urls['logout']

if __name__ == '__main__':
    app = Postpost('postpost', 'xyz.trsq.postpost')
    app.main_loop()
