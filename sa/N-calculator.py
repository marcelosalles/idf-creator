# N calculator

SIMULATIONS = 30000

def Ncalc(D, type = 'bldg', simulations = 30000):

    if type == 'uni':

        cases = simulations*(1/5)*6

    elif type == 'bot' or type == 'top':

        cases = simulations*(4/5)*6

    elif type == 'mid':

        cases = simulations*(1+2+3)*(1/5)*6

    elif type == 'blgd':

        cases = simulations

    elif type == 'room':

        cases = simulations*(1+2+3+4+5)*(1/5)*6

    N = cases/(D + 2)

    return int(N)

# print('uni',Ncalc(15,'uni'))
# print('bot',Ncalc(14,'bot'))
# print('mid',Ncalc(14,'mid'))
# print('top',Ncalc(15,'top'))
print('blgd',Ncalc(5,'blgd'))
print('room',Ncalc(3,'room'))