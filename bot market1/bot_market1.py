from operator import index
import sqlite3
import flet as ft 


def main(page: ft.Page):
    page.title="Sm0keRTM"
    page.theme_mode="dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width=400
    page.window_height=400
    page.window_resizable=False
    
    def register(e):
        db=sqlite3.connect('Sm0k')
        
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRYMARY KEY,
                    login TEXT,
                    pass TEXT
        )""")
        cur.execute(F"INSERT INTO users VALUES(NULL, '{user_login.value}','{user_pass.value}')")
                                                      
        db.commit()
        db.close()
        
        user_login.Value=''
        user_pass.Value=''
        btn_Reg.Value='Add'
        page.update()

    def validate(e):
        if all([user_login.value,user_pass.value]):
            btn_Reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_Reg.disabled = True
            btn_auth.disabled = True
        page.update()
        
    def auth_user(e):
        db=sqlite3.connect('Sm0k')
        
        cur = db.cursor()
        cur.execute(F"SELECT * FROM users WHERE login = '{user_login.value}'AND pass = '{user_pass.value}'")
        if cur.fetchone() != None:
            user_login.value=''
            user_pass.value=''
            btn_auth.text = 'Authorization'
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Eror!'))
            page.snack_bar.open = True
            page.update()

        db.commit()
        db.close()
        
    user_login = ft.TextField(label='login',width=200,on_change=validate)
    user_pass = ft.TextField(label='password',password=True,width=200,on_change=validate)
    btn_Reg=ft.OutlinedButton(text='Add',width=200,on_click=register,disabled=True)
    btn_auth=ft.OutlinedButton(text='Authorization',width=200,on_click=auth_user,disabled=True)
    
    panel_register= ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Registration'),
                    user_login,
                    user_pass,
                    btn_Reg
                ]
             )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    panel_auth= ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Authorization'),
                    user_login,
                    user_pass,
                    btn_auth
                ]
             )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()
        
        if index ==0:page.add(panel_register)
        elif index ==1:page.add(panel_auth)    

    page.navigation_bar= ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Registration"),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Authorization")
            ],on_change= navigate
        )



    page.add(panel_register)


ft.app(target=main)    

#main panel 
def main_panel(page: ft.Page):
    page.title="Sm0keRTM"
    page.theme_mode="dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width=800
    page.window_height=600
    page.window_resizable=False    
   

    page.add()
    
ft.app(target=main_panel) 
