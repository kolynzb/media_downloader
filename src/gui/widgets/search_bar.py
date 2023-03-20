import flet as ft


class SearchBar(ft.UserControl):
    def build(self):
        self.textField = ft.TextField(width=80)
        self.searchButton = ft.FloatingActionButton(icon=ft.icons.ADD,onclick=self.sum_func)

        task_row = ft.Row(controls=[self.textField,self.searchButton])
        return task_row
    
    def sum_func(self,e):
        pass
