'''
@FileName:好获商城总表修改脚本

@Author：毛向官

@Create date:2018-7-19

@description：数量太多，重复操作，脚本操作

@version：1.0
'''


from selenium import webdriver
from time import sleep
import config


class Instantiation():
    def __init__(self):
        # 实行登录操作
        self.Boswer = webdriver.Chrome()
        self.Boswer.set_window_size(1920, 1000)
        self.Boswer.get("http://zsadmin.hoshiibuy.com/admin/")
        username = self.Boswer.find_element_by_name("account")
        pwd = self.Boswer.find_element_by_name("password")
        username.send_keys("18558728101")
        pwd.send_keys("123456")
        login = self.Boswer.find_element_by_class_name("m-b")
        login.click()
        self.inventory_modification()

    # 进入商品列表
    def inventory_modification(self):
        for Commodity_coding in config.off_sale[1:]:
            self.Boswer.get("http://zsadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            print(Commodity_coding)
            search_info.clear()
            search_info.send_keys(Commodity_coding)
            sleep(2)  #网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_class_name("glyphicon-search")
            search_btn.click()
            sleep(1)
            table = self.Boswer.find_element_by_id("DataTables_Table_0")
            # table_rows = table.find_elements_by_tag_name("tr")
            # table_cols = table_rows[0].find_elements_by_tag_name('th')
            btn2 = table.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]/td[12]/button[1]")
            url = "http://zsadmin.hoshiibuy.com/" + btn2.get_attribute("data-url")
            self.change_info(url, -1, 0, 0, 0)
        for Commodity_coding in config.Honsale[1:]:
            self.Boswer.get("http://zsadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            print(Commodity_coding)
            search_info.clear()
            Commodity_id = Commodity_coding[0]
            count = Commodity_coding[1]
            pri = Commodity_coding[2]
            rebate = Commodity_coding[3]
            search_info.send_keys(Commodity_id)
            sleep(2)  #网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_id("search")
            search_btn.click()
            sleep(1)
            table = self.Boswer.find_element_by_id("DataTables_Table_0")
            # table_rows = table.find_elements_by_tag_name("tr")
            # table_cols = table_rows[0].find_elements_by_tag_name('th')
            btn2 = table.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]/td[12]/button[1]")
            url = "http://zsadmin.hoshiibuy.com/" + btn2.get_attribute("data-url")
            self.change_info(url, 0, count, pri, rebate)

    def change_info(self, url, order_num, count, pri, rebate):
        sleep(2)
        self.Boswer.get(url)
        if order_num == 0:
            price = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[8]/div[1]/input')
            rebate1 = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[8]/div[2]/input')
            price.clear()
            price.send_keys(pri)
            rebate1.clear()
            rebate1.send_keys(rebate)
        # 权重
        weight = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[14]/div[1]/input')
        weight.clear()
        weight.send_keys(order_num)
        sleep(1)
        # 库存
        Stock = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[14]/div[2]/input')
        Stock.clear()
        Stock.send_keys(count)
        sleep(1)
        # 保存操作
        btn3 = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[36]/div/button[1]')
        btn3.click()
        sleep(2)
        print("页面修改成功")


if __name__ == "__main__":
    Instantiation()