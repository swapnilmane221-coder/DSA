class Solution(object):

    def toHex(self, num):
        if num==0:
            return "0"
        if num < 0:
            num = (1 << 32) + num
        hexaval=""
        l_dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

        while num!=0:
            rem=num%16
            if rem in l_dict:
                hexaval=l_dict[rem]+hexaval
            else:
                hexaval=str(rem)+hexaval
            num//=16
        return hexaval
        