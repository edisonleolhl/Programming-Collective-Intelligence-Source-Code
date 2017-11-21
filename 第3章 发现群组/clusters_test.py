import clusters

# pprint(clusters.readfile('blogdata.txt'))
blognames, words, data = clusters.readfile ('blogdata.txt')
clust = clusters.hcluster (data)
# clusters.printclust(clust, labels=blognames)

# k-means
kclust1 = clusters.kcluster (data, k=10)
# pprint([[blognames[i] for i in kclust[j]] for j in range(10)])
kclust2, clusters_pos = clusters.kcluster_exercise (data, k=10)
# pprint(clusters_pos)

# clusters on preferences
wants, people, data = clusters.readfile ('zebo.txt')
clust = clusters.hcluster (data, distance=clusters.tanamoto)
clusters.drawdendrogram (clust, wants)
