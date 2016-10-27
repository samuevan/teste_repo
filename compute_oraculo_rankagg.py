import sys
import glob


def read_ranking(ranking_file):

    users_rankings = {}
    ranking_handler = open(ranking_file)
    for line in ranking_handler:
        tokens = line.strip().split('\t')
        user = int(tokens[0])
        items = tokens[1].strip().replace('[','').replace(']','').split(',')
        users_rankings[user] = []
        for item_score in items:
            item = int(item_score.split(':')[0])
            users_rankings[user].append(item)

    return users_rankings            



def read_test(test_file):

    data = open(test_file,'r')
    past_usr,past_mov,past_rat = data.readline().strip().split('\t')
    line_usr = past_mov

    users_test = {int(past_usr):[(int(past_mov),int(past_rat))]}


    nusers = 1;
    for line in data:
        usr,mov,rat = line.strip().split('\t')
        
        if usr == past_usr:

            users_test[int(usr)].append((int(mov),int(rat)))
            #line_usr += ' '+mov
            past_usr,past_mov = usr,mov
        else:
            users_test[int(usr)] = [(int(mov),int(rat))]
            nusers += 1
            past_usr,past_mov = usr,mov

    return users_test



def num_total_hits(rankings,test,hits_set,size):

    total_hits = 0;
    
    for user in rankings.keys():
        if not hits_set.has_key(user):
            hits_set[user] = set()            

        
        if test.has_key(user):
            test_user = [x for x,_ in test[user]]
            rank_user = rankings[user]
            for i in range(size):
                if rank_user[i] in test_user:
                    hits_set[user].add(rank_user[i])
                    total_hits += 1
                

      

    return total_hits





#def run(basedir):





if __name__ == "__main__":

    basedir = sys.argv[1]
    rank_size = 10
    if len(sys.argv) > 2:
        rank_size = int(sys.argv[2])
#    run(basedir)

    for part in range(1,6):
        partition = "u"+str(part)
        files = sorted(glob.glob(basedir+partition+"*.out"))
        test = read_test(basedir+partition+'.test')

        #print files
        #print "\t\t\tmap@10\tp@1\tp@5\tp@10\tNDCG\thits\tavg hits"

        print "Part"+str(part)+"\n\n"

        hits_set = {}
        hits_by_rank = []
        for f in files:
            data = read_ranking(f)
            hits_rank = num_total_hits(data,test,hits_set,rank_size)
            hits_by_rank.append(hits_rank)
            print f.split("\\")[-1]+": " + str(hits_rank)

        
        num_hits = 0;
        for user in hits_set.keys():
            num_hits += len(hits_set[user])


        print "Total" + str(num_hits)

        #print "Total hits: " + str(sum(hits_by_rank))
        


