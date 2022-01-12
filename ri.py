list_dup=[{'customer_name': 'rishi', 'product_id': 2451}, {'customer_name': 'varun', 'product_id': 4032},
 {'customer_name': 'rishi', 'product_id': 5255}, {'customer_name': 'varun', 'product_id': 4032}]
list_nodup = []
for i in range(len(list_dup)):
	if list_dup[i] not in list_dup[i + 1:]:
		list_nodup.append(list_dup[i])
print (list_nodup)