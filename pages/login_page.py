from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.open(), "login is absent in current url"

    def should_be_login_form(self):
        assert "login-username" in self.open(), "NotFoundLogin"

    def should_be_register_form(self):
        assert "registration-email" in self.open(), "NotFoundRegistration"