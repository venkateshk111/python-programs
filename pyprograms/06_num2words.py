# Python program to convert number to words ( between 1 and 99)

upto_19 = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']

tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']

output = ''

num = int(input('Please enter number between 1 and 99: '))

if num == 0 :
    output = 'ZERO'
elif num <= 19 :
    output = upto_19[num]
elif num <=99 :
    output = tens[num // 10]+" "+upto_19[num%10]
else :
    output = '\nPlease enter number between 1 and 99 only'

print(output)
