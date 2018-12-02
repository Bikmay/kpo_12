import random
import networkx as nx
import matplotlib.pyplot as plt

class A():

    alphas=[]
    handing_nodes=[]
    count_nodes_grafs=[]

    def count_child_node (is_random,o):
        if(is_random):
            return random.randint(0, o)
        else:
            return o


    def create_graf(count_child_nodes,count_nodes,is_random_child_node=True):
        print("\n---------------------------------------------------------------------------------------")

        nodes =[1]


        k=0 #индекс актуального элемента

        current_count_node=1
        count_child_nodes_now=0

        mass_count_child_nodes=[]
        node=1


        mass_handing_nodes=[]
        G = nx.Graph()

        G.add_node(1)

        A.count_nodes_grafs.append(count_nodes)
        print(count_nodes)


        while(current_count_node<count_nodes):
            count_child_nodes_now=A.count_child_node(is_random_child_node,count_child_nodes)

            if(count_child_nodes_now+current_count_node>count_nodes):
                count_child_nodes_now = count_nodes - current_count_node

            if(count_child_nodes_now==0 ):
                mass_count_child_nodes.append(count_child_nodes_now)
                mass_handing_nodes.append(nodes[k-1])
                nodes.append(1 + len(nodes))
                k+=1
                continue

            if(current_count_node+count_child_nodes_now<=count_nodes):
                mass_count_child_nodes.append(count_child_nodes_now)

                for i in range(count_child_nodes_now):
                    node+=1
                    nodes.append(1 + len(nodes))
                    G.add_node(node)
                    G.add_edge(nodes[k],node)

                    # print(str(nodes[k])+ "-"+str(node))
                k += 1
            current_count_node+=count_child_nodes_now



        for i in range(len(nodes) - k):
            mass_handing_nodes.append(nodes[k+i])

        print("nodes")
        print(G.nodes)

        print("handing nodes")
        print(mass_handing_nodes)

        A.handing_nodes.append(len(mass_handing_nodes))
        alpha=count_nodes/len(mass_handing_nodes)
        A.alphas.append(alpha)
        print(alpha)

        print("count handing nodes "+str(len(mass_handing_nodes)))

        print("count levels graf") #пока хз как но я в процессе, скоро будет

        print("связи по красоте")
        print(G.edges) #тут выводится все связи по красоте

        print("\n---------------------------------------------------------------------------------------")
        return

        nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

        plt.savefig("edge_colormap.png")
        plt.show()

        A.create_gist(mass_count_child_nodes)

        print("\n---------------------------------------------------------------------------------------")



    #даже можешь не начинать разбираться в этом
    def create_gist(counts):

            # max_x= (count%10)+1
            x = []

            # Самый бессмысленный цикл в мире
            for i in range(len(counts)):
                x.append(i)

            # i=1
            # for i in range(max_x):
            #    x.append(i*10)

            er = range(len(counts))
            ax = plt.gca()
            ax.bar(er, counts, align="edge")
            ax.set_xticks(er)

            print(len(counts))
            print(counts)
            # width=x
            # plt.bar(len(counts), counts, width,align="edge")
            # plt.xticks(x)
            plt.show()
