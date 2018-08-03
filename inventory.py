'''
@FileName:严选总表操作

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
        self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/")
        username = self.Boswer.find_element_by_name("account")
        pwd = self.Boswer.find_element_by_name("password")
        username.send_keys("18558728101")
        pwd.send_keys("zhuni123456")
        login = self.Boswer.find_element_by_class_name("m-b")
        login.click()
        self.inventory_modification()

    # 进入商品列表
    def inventory_modification(self):
        for Commodity_coding in config.off_sale[1:]:
            sleep(2)
            self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            print(Commodity_coding)
            search_info.clear()
            search_info.send_keys(Commodity_coding)
            sleep(2)  #网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_class_name("glyphicon-search")
            search_btn.click()
            sleep(1)
            table = self.Boswer.find_element_by_id("tables")
            # table_rows = table.find_elements_by_tag_name("tr")
            # table_cols = table_rows[0].find_elements_by_tag_name('th')
            btn2 = table.find_element_by_xpath("//*[@id='tables']/tbody/tr/td[13]/button[1]")
            url = "http://yxadmin.hoshiibuy.com/" + btn2.get_attribute("data-url")
            self.change_info(url, -1, 0, 0, 0, 0)

        #上架
        for Commodity_coding in config.on_sale[1:]:
            sleep(2)
            Commodity_id = Commodity_coding[0]
            count = Commodity_coding[1]
            pri = Commodity_coding[2]
            rebate = Commodity_coding[3]
            sf = Commodity_coding[4]
            self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            print(Commodity_id)
            search_info.clear()
            search_info.send_keys(Commodity_id)
            sleep(2)  #网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_class_name("glyphicon-search")
            search_btn.click()
            # on_sale = self.Boswer.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[13]/button[4]')
            # on_sale.click()
            # on_sale2 = self.Boswer.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]')
            # on_sale2.click()
            sleep(1)
            table = self.Boswer.find_element_by_id("tables")
            btn2 = table.find_element_by_xpath("//*[@id='tables']/tbody/tr/td[13]/button[1]")
            url = "http://yxadmin.hoshiibuy.com/" + btn2.get_attribute("data-url")
            self.change_info(url, 0, count, pri, rebate, sf)

        # 供应商推荐奖
        for supply_price in config.suppliy_price[1:]:
            self.Boswer.get("http://yxadmin.hoshiibuy.com/admin/product/go/list-product")
            search_info = self.Boswer.find_element_by_name("serial")
            Commodity_coding, senior, Blue, red = supply_price
            print(Commodity_coding)
            search_info.clear()
            search_info.send_keys(Commodity_coding)
            sleep(2)  # 网页反应不过来，设置2S间隔
            search_btn = self.Boswer.find_element_by_class_name("glyphicon-search")
            search_btn.click()
            sleep(1)
            self.change_supplier(senior, Blue, red)

    def change_supplier(self, seniors, Blues, reds):
        btn4 = self.Boswer.find_element_by_xpath("//*[@id='tables']/tbody/tr/td[13]/button[8]")
        btn4.click()
        sleep(1)
        senior = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[4]/div/input")
        Blue = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[5]/div/input")
        red = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[6]/div/input")
        purple = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[7]/div/input")
        black = self.Boswer.find_element_by_xpath("//*[@id='add-supplier-modal']/div/div/div[1]/div[8]/div/input")
        # 清楚输入框信息
        senior.clear()
        Blue.clear()
        red.clear()
        purple.clear()
        black.clear()
        # 输入供应商推荐奖
        sleep(1)
        senior.send_keys(seniors)
        Blue.send_keys(Blues)
        red.send_keys(reds)
        purple.send_keys(reds)
        black.send_keys(reds)
        # 保存操作
        save_btn = self.Boswer.find_element_by_xpath("//*[@id='add-product-submit-btn']")
        sleep(2)
        save_btn.click()
        print("供应商修改成功")

    def change_info(self, url, order_num, count, pri, rebate, shuf):
        sleep(2)
        self.Boswer.get(url)
        if order_num == 0:
            price = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[8]/div[1]/input")
            rebate1 = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[8]/div[2]/input')
            shuifei = self.Boswer.find_element_by_xpath('//*[@id="submitForm"]/div/div[2]/div[10]/div/input')
            price.clear()
            price.send_keys(pri)
            rebate1.clear()
            rebate1.send_keys(rebate)
            shuifei.clear()
            shuifei.send_keys(shuf)
        # 权重
        weight = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[18]/div[1]/input")
        weight.clear()
        weight.send_keys(order_num)
        sleep(1)
        # 库存
        Stock = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[18]/div[2]/input")
        Stock.clear()
        Stock.send_keys(count)
        sleep(1)
        # 保存操作
        btn3 = self.Boswer.find_element_by_xpath("//*[@id='submitForm']/div/div[2]/div[40]/div/button[1]")
        btn3.click()
        sleep(2)
        print("页面修改成功")


if __name__ == "__main__":
    Instantiation()