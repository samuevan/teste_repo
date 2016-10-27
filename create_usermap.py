#This script converts data in the format of movielens dataset in the input format required by the lda
#also outputs the usermap, that maps each user to a position in the lda input file
#and the words distribuction

import sys

def main(input_f):
    data = open(input_f,'r')
        
    #output = open(input_f + '.lda','w')
    out_map = open(input_f + '.usermap','w')
    #out_movies_freq = open(input_f + '.freq','w')
    #movies_freq = {}

    past_usr,past_mov,past_rat = data.readline().strip().split('\t')
    out_map.write(past_usr+'\t'+str(0)+'\n')
    #movies_freq[int(past_mov)] = 1

    line_usr = past_mov
    #nratings = 1
    nusers = 1;
    for line in data:
        usr,mov,rat = line.strip().split('\t')
        
        #counting words frequency    
        '''if movies_freq.has_key(int(mov)):
            movies_freq[int(mov)] += 1
        else:
            movies_freq[int(mov)] = 1
        '''
        #creating user line
        if usr == past_usr:
            line_usr += ' '+mov
            past_usr,past_mov = usr,mov
        else:
            out_map.write(str(usr)+'\t'+str(nusers)+'\n')
            nusers += 1
            #output.write(line_usr+'\n')
            line_usr += '\n'
            line_usr += mov #it's gonna fail if the last user was rated just one movie            
            past_usr,past_mov = usr,mov
        #nratings += 1

    '''for key in movies_freq.keys():
        movies_freq[key] = float(movies_freq[key])/nratings
        out_movies_freq.write(str(key)+'\t'+str(movies_freq[key])+'\n')
    '''
    

    #output.write(str(nusers)+'\n')
    #output.write(line_usr) #writes the last user
    #out_movies_freq.close()
    #data.close()
    #output.close()
    out_map.close()


if __name__ == '__main__':
    input_f = sys.argv[1]
    main(input_f)


