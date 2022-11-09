from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

block_min = 12965000
block_max = 15282336
blocks = 0
unc_blocks = 0


random_list = random.sample(range(block_min,block_max+1), 1000)

driver = webdriver.Chrome(ChromeDriverManager().install())

for block in random_list:    
    print(block)
    try:
        driver.get("https://etherscan.io/block/" + str(block))
        assert "Ethereum Blocks #"+str(block)+" | Etherscan" in driver.title 
    except:
        print('Last block: ', str(block-1))
        print('Unc blocks: ', str(unc_blocks))
        print('Total blocks: ', str(blocks))
        time.sleep(10)
        driver.get("https://etherscan.io/block/" + str(block))
        assert "Ethereum Blocks #"+str(block)+" | Etherscan" in driver.title 
        #exit()
    try:
        order = driver.find_element("xpath", "//a[@class='mb-1 mb-sm-0 u-label u-label--xs u-label--indigo']")
        if order.text == 'Unconventional Ordering':
            unc_blocks = unc_blocks+1
    except: 
        continue
    blocks = blocks + 1

print('Last block: ', str(block-1))
print('Unc blocks: ', str(unc_blocks))
print('Total blocks: ', str(blocks))