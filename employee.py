class Employee:
    raise_amt=1.04
    def __init__(self,frist,last,pay):
        self.frist=frist
        self.last=last
        self.email=frist+'.'+last+'@gmail.com'
        self.pay=pay
    def fullname(self):
        return'{} {}'.format(self.frist,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,frist,last,pay,pro_lang):
        super().__init__(frist,last,pay)
        self.pro_lang=pro_lang
class Manager(Employee):
    def __init__(self,frist,last,pay,employees=None):
        super().__init__(frist,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
    def remove_emp(self,emp):
            if emp not in self.employees:
                self.employees.remove(emp)
    def print_emps(self):
        for self.emp in self.employees:
            print(self.fullname())
dev_1=Developer('amr','ibrahim',20000,'python')
dev_2=Manager('ali','omar',40000,['pop'])
print(dev_1.pay)
print(dev_2.apply_raise())
dev_2.print_emps()
dev_2.fullname()
dev_2.add_emp('to')
print(dev_2.employees)

