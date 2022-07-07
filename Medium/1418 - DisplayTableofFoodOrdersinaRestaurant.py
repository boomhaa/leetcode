# link to the problem - https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.
# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

# link to submission - https://leetcode.com/submissions/detail/740702054/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        resp = dict()
        items = set()
        s = []
        orders.sort(key=lambda x: int(x[1]))
        for ord in orders:
            if ord[1] not in resp:
                resp[ord[1]] = []
            resp[ord[1]].append(ord[2])
            items.add(ord[2])
        items = list(["Table"]) + sorted(items)
        s.append(items)
        for k,v in resp.items():
            r = [k]
            for i in items:
                if i != "Table":
                    r.append(str(v.count(i)))
            s.append(r)
        return (s)