import random
import networkx as nx
import matplotlib.pyplot as plt
import ij as q

class A():

    alphas=[]
    handing_nodes=[]
    count_nodes_grafs=[]
    height_graf=[]

    alphas_on_each=[]
    nodes_count_on_each=[]

    def count_child_node (is_random,o):
        if(is_random):
            return random.randint(0, o)
        else:
            return o


    def create_graf(count_child_nodes,count_nodes,is_random_child_node=True, is_final=False):

        f=open("out.txt",'w')
        print("\n---------------------------------------------------------------------------------------")
        f.write("\n---------------------------------------------------------------------------------------"+'\n')
        nodes =["0-1"]


        k=0 #индекс актуального элемента

        count_child_nodes_now=0

        mass_count_child_nodes=[]
        node=1


        mass_handing_nodes=[]
        G = nx.Graph()

        G.add_node("0-1")

        A.count_nodes_grafs.append(count_nodes)
        f.write(str(count_nodes)+'\n')
        print(count_nodes)


        while(node<count_nodes):
            count_child_nodes_now=A.count_child_node(is_random_child_node,count_child_nodes)
            #КОСТЫЛЬ на случай если у корневой ноды нарандомится нуль дочерних элементов
            if(count_child_nodes_now==0 & node==1):
                return #вычитал в методичке

            if(count_child_nodes_now==0 ):
                mass_count_child_nodes.append(count_child_nodes_now)
                mass_handing_nodes.append(str(k+1) + '-' + str(node))
                nodes.append(str(k+1) + '-' + str(node))
                k+=1 #надо убрать
                node+=1
                continue

            if (count_child_nodes_now + len(nodes) > count_nodes):
                count_child_nodes_now = count_nodes - node

            mass_count_child_nodes.append(count_child_nodes_now)

            for i in range(count_child_nodes_now):
                node+=1
                nodes.append(str(k+1) + '-' + str(node))
                G.add_node(str(k+1) + '-' + str(node))
                G.add_edge(nodes[k], str(k+1) + '-' + str(node))
                if is_final:
                    A.alphas_on_each.append(A.ifFinal(len(nodes), len(nodes) - k + 1 + len(mass_handing_nodes)))
                    A.nodes_count_on_each.append(len(nodes))
               # print(str(nodes[k])+ "-"+str(node))
            k += 1



        for i in range(len(nodes) - k):
            mass_handing_nodes.append(nodes[k+i])

        if is_final:
            A.alphas_on_each.append(A.ifFinal(len(nodes)+1, len(mass_handing_nodes)))
            A.nodes_count_on_each.append(len(nodes))

        # print("debug")
        # print(mass_count_child_nodes)
        print("nodes")
        print(G.nodes)
        f.write("nodes\n")
        f.write(str(G.nodes) + "\n")

        print("handing nodes")
        print(str(mass_handing_nodes))
        f.write("handing nodes"+'\n')
        f.write(str(mass_handing_nodes)+'\n')


        A.handing_nodes.append(len(mass_handing_nodes))
        alpha=count_nodes/len(mass_handing_nodes)
        A.alphas.append(alpha)
        print("alpha")
        print(alpha)
        f.write("alpha\n")
        f.write(str(alpha) + "\n")

        print("count handing nodes "+str(len(mass_handing_nodes)))
        f.write("count handing nodes "+str(len(mass_handing_nodes))+'\n')

        print("count levels graf")
        f.write("count levels graf ")
        io=q.count_height()

        print(io)
        f.write(str(io) + "\n")
        A.height_graf.append(io)


        f.write("\n---------------------------------------------------------------------------------------"+'\n')

        print("\n---------------------------------------------------------------------------------------")
        # return
        print(G.edges)
        nx.draw(G, with_labels=True, node_color="blue", alpha=0.6, node_size=50)

        plt.savefig("edge_colormap.png")
        plt.show()

        A.create_gist(mass_count_child_nodes)
        f.close()
        print("\n---------------------------------------------------------------------------------------")
        return



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

    def sum(mass):
        a=0
        for i in range(len(mass)):
           a+=mass[i]

        return a

    def ifFinal(nodes, handing_nodes):
        return nodes/handing_nodes
