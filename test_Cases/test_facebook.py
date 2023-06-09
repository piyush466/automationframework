from pageobject.Loginpage import LoginP


class Test_001:
    username = 'piyush@gmail.com'
    password = 'piyush@123'

    def test_login(self,setup):
        self.driver= setup
        self.lp = LoginP(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        print("test")

