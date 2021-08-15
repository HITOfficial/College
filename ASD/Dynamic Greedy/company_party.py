# Exercise in PL lang.
# Proszę zaimplementować rozwiązanie problemu “Impraza firmowa” tak, by zwracane były imiona pracowników, którzy idą na imprezę.
# Należy założyć, że pracownicy reprezentowani są w strukturze:

# complexity:
# - time O(N)
# - space O(N*K), where K are a number of children of every node


class Employee:
    def __init__(self, fun, name, emp=[]):
        self.emp = emp
        self.fun = fun
        self.name = name
        # if f / g have None value, that means, was'nt visited before
        self.f = None
        self.g = None
        self.f_path = [name]
        self.g_path = []

    # bottom up alg.
    # F(x) =  max(sum(G(k))+x.fun, sum(F(k))), where k are children of x node
    def F(self):
        if self.f is None:
            self.f = self.fun
            F_children, children_path = 0, []
            for children in self.emp:
                children.F()
                children.G()
                F_children += children.f
                children_path.extend(children.f_path)
                self.f_path.extend(children.g_path)
                self.f += children.g
            # checking if single chindren F function was beter than actual node F function
            if F_children > self.f:
                self.f, self.f_path = F_children, children_path

    # G(x) =  sum(F(k)), where k are children of x node
    def G(self):
        if self.g is None:
            self.g = 0
            for children in self.emp:
                children.F()
                children.G()
                self.g += children.f
                self.g_path.extend(children.f_path)


# test data
n18 = Employee(1, 18)
n17 = Employee(2, 17, [n18])
n14 = Employee(3, 14, [n17])
n16 = Employee(12, 16)
n13 = Employee(7, 13, [n16])
n11 = Employee(17, 11, [n13, n14])
n15 = Employee(4, 15)
n12 = Employee(16, 12)
n10 = Employee(5, 10, [n11, n12])
n8 = Employee(2, 8)
n7 = Employee(1, 7)
n6 = Employee(26, 6)
n2 = Employee(4, 2, [n6, n7, n8])
n3 = Employee(30, 3, [n10])
n4 = Employee(17, 4)
n9 = Employee(8, 9)
n5 = Employee(5, 5, [n9])
n1 = Employee(16, 1, [n4, n5])
n0 = Employee(6, 0, [n1, n2, n3])


def company_party(root):
    root.F()
    root.G()
    # returning total sum, nodes name from best option
    if root.f > root.g:
        return root.f, root.f_path
    else:
        return root.g, root.g_path


print(company_party(n0))
