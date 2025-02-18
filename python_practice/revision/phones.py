phones = ['tecno', 'infinix', 'samsung']
print(phones)

phones.append('xiaomi')
phones.append('redmi')
phones.append('nokia')
print(phones)

phones.insert(2, '"mapangale"')
phones.insert(-1, 'motorolla')
print(phones)

del phones[0]
print(phones)

popped_phones = phones.pop()
print(phones)
print(popped_phones)
print(f"the latest phone in the market is {popped_phones.title()}")

last_owned_phone = phones.pop(2)
print(f"the last owned phone which got stolen is {last_owned_phone.title()}")

fake_phone = '"mapangale"'
phones.remove('"mapangale"')
print(phones)
print(f"\nThe {fake_phone.upper()} does not exist in the market of phones")
