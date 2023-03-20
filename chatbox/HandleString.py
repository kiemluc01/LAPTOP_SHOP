import re


# convert accent vietnamese to no
def no_accent_vietnamese(s):
    s = s.lower()
    #config a
    s = re.sub('[a][a]', 'â', s)
    s = re.sub('[a][f]', 'à', s)
    s = re.sub('[a][s]', 'á', s)
    s = re.sub('[a][r]', 'ả', s)
    s = re.sub('[a][x]', 'ã', s)
    s = re.sub('[a][j]', 'ạ', s)
    
    # config ă
    s = re.sub('[â][f]', 'ầ', s)
    s = re.sub('[â][s]', 'ấ', s)
    s = re.sub('[â][r]', 'ẩ', s)
    s = re.sub('[â][x]', 'ẫ', s)
    s = re.sub('[â][j]', 'ậ', s)
    s = re.sub('[à][a]', 'ầ', s)
    s = re.sub('[á][a]', 'ấ', s)
    s = re.sub('[ả][a]', 'ẩ', s)
    s = re.sub('[ã][a]', 'ẫ', s)
    s = re.sub('[ạ][a]', 'ậ', s)
    # config ă
    s = re.sub('[a][w]', 'ă', s)
    s = re.sub('[ă][f]', 'ằ', s)
    s = re.sub('[ă][s]', 'ắ', s)
    s = re.sub('[ă][r]', 'ẳ', s)
    s = re.sub('[ă][x]', 'ẵ', s)
    s = re.sub('[ă][j]', 'ặ', s)
    s = re.sub('[à][w]', 'ằ', s)
    s = re.sub('[á][w]', 'ắ', s)
    s = re.sub('[ả][w]', 'ẳ', s)
    s = re.sub('[ã][w]', 'ẵ', s)
    s = re.sub('[ạ][w]', 'ặ', s)
    
    # config ê
    s = re.sub('[e][e]', 'ê', s)
    s = re.sub('[e][f]', 'è', s)
    s = re.sub('[e][s]', 'é', s)
    s = re.sub('[e][r]', 'ẻ', s)
    s = re.sub('[e][x]', 'ẽ', s)
    s = re.sub('[e][j]', 'ẹ', s)
    
    # config ê
    s = re.sub('[ê][f]', 'ề', s)
    s = re.sub('[ê][s]', 'ế', s)
    s = re.sub('[ê][r]', 'ể', s)
    s = re.sub('[ê][x]', 'ễ', s)
    s = re.sub('[ê][j]', 'ệ', s)
    s = re.sub('[è][e]', 'ề', s)
    s = re.sub('[é][e]', 'ế', s)
    s = re.sub('[ẻ][e]', 'ể', s)
    s = re.sub('[ẽ][e]', 'ễ', s)
    s = re.sub('[ẹ][e]', 'ệ', s)
    
    # config o 
    s = re.sub('[o][o]', 'ô', s)
    s = re.sub('[o][f]', 'ò', s)
    s = re.sub('[o][s]', 'ó', s)
    s = re.sub('[o][r]', 'ỏ', s)
    s = re.sub('[o][x]', 'õ', s)
    s = re.sub('[o][j]', 'ọ', s)
    
    # config ô
    s = re.sub('[ô][f]', 'ồ', s)
    s = re.sub('[ô][s]', 'ố', s)
    s = re.sub('[ô][r]', 'ổ', s)
    s = re.sub('[ô][x]', 'ỗ', s)
    s = re.sub('[ô][j]', 'ộ', s)
    s = re.sub('[ò][o]', 'ồ', s)
    s = re.sub('[ó][o]', 'ố', s)
    s = re.sub('[ỏ][o]', 'ổ', s)
    s = re.sub('[õ][o]', 'ỗ', s)
    s = re.sub('[ọ][o]', 'ộ', s)
    
    # config u 
    s = re.sub('[u][w]', 'ư', s)
    s = re.sub('[u][f]', 'ù', s)
    s = re.sub('[u][s]', 'ú', s)
    s = re.sub('[u][r]', 'ủ', s)
    s = re.sub('[u][x]', 'ũ', s)
    s = re.sub('[u][j]', 'ụ', s)
    
    # config ư
    s = re.sub('[ư][f]', 'ừ', s)
    s = re.sub('[ư][s]', 'ứ', s)
    s = re.sub('[ư][r]', 'ử', s)
    s = re.sub('[ư][x]', 'ử', s)
    s = re.sub('[ư][j]', 'ự', s)
    s = re.sub('[ù][w]', 'ừ', s)
    s = re.sub('[ú][w]', 'ứ', s)
    s = re.sub('[ủ][w]', 'ử', s)
    s = re.sub('[ũ][w]', 'ử', s)
    s = re.sub('[ụ][w]', 'ự', s)
    
    s = re.sub('[d][d]', 'd', s)
    return s

def like(a, b):
    b = b.split(" ")
    for i in b:
        if i == a:
            return True
    return False

# find a like b
def same(a,b):
    a = a.split(" ")
    for i in a:
        if not like(i, b):
            return False
    return True
def no_vietnamese(s):
    s = s.lower()
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('đ', 'd', s)
    return s
# check list a like b 
def check(a,b):
    for i in a:
        if same(i,b) or same(b,i) or same(no_vietnamese(i),b):
            return True
    return False

