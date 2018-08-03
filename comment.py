'''
@FileName:新增评论

@Author：毛向官

@Create date:2018-7-19

@version：1.0
'''

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import config


class Instantiation():
    def __init__(self):
        # 实行登录操作
        self.Boswer = webdriver.Chrome()
        self.Boswer.set_window_size(1920, 1000)
        self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/")
        username = self.Boswer.find_element_by_name("account")
        pwd = self.Boswer.find_element_by_name("password")
        username.send_keys("18558728101")
        pwd.send_keys("zhuni123456")
        login = self.Boswer.find_element_by_class_name("m-b")
        login.click()
        self.add_commont()

    def add_commont(self):
        for cmts in config.commont_arr[1:]:
            self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/evaluate/go/nom-backstage-evaluate?id=0")
            com_id, coms, nickname = cmts
            btn = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div[2]/div[2]/a")
            btn.click()
            sleep(1)
            input1 = self.Boswer.find_element_by_xpath("//*[@id='name']")
            input1.send_keys(com_id)
            searchbtn = self.Boswer.find_element_by_id("search")
            searchbtn.click()
            table = self.Boswer.find_element_by_id("DataTables_Table_0_wrapper")
            n = 1
            inputs = table.find_elements_by_tag_name('input')
            # 然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
            for inp in inputs:
                if inp.get_attribute('type') == 'checkbox':
                    if inp.is_selected() == False and n == 2:
                        ActionChains(inp).click()
                    n += 1
            print(1)

        pass


if __name__ == "__main__":
    Instantiation()