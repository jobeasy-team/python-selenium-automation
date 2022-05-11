# CSS selector for Amazon Create Account Page

Amazon_logo = (By.CSS_Selector, "div.a-section.a-spacing-medium.a-text-center [href*='ap_frn_logo'] [class='a-icon a-icon-logo']")
# A bit long but I wanted to see how specific i could be

Create_Account_Logo = (By.CSS_Selector, "div.a-box-inner [class='a-spacing-small']")

your_name = (By.CSS_Selector, 'div.a-row.a-spacing-base input#ap_customer_name')

mob_email = (By.CSS_Selector, 'span.a-declarative input#ap_email')

pwd = (By.CSS_Selector, 'div.a-row.a-spacing-base input#ap_password')

re_pwd = (By.CSS_Selector, 'input#ap_password_check')

cont_btn = (By.CSS_Selector, 'input#continue')

conditions_o_u = (By.CSS_Selector, "#legalTextRow [href*='condition']'")

privacy = (By.CSS_Selector, "#legalTextRow [href*='privacy']'")

lower_signin = (By.CSS_Selector, 'div.a-row a.a-link-emphasis')
# this selector gave 2 outputs but I still found it acceptible since they lead to the same place
