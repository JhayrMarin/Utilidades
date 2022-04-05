from passlib.context import CryptContext
septpw = CryptContext(schemes=['pbkdf2_sha512'])
clave=septpw.encrypt('admin')
print(clave)

# select * from res_users where id=2
# update res_users set password='$pbkdf2-sha512$25000$EkLo3TsnhPBeyznH2BujdA$.0cghQJfsQoTEGg/eVFgxlMkga4Xct.Mf9wwQp0q6qnma4DtvqmHTyvvitBB/0kRjeNdJhBVrM9.xLUog1JseQ' where id=2

