import numpy as np


def non_maximum_supression(boxes , overlapthresh):

	if len(boxes)==0:
		return []

	# if the bounding boxes integers, convert them to floats --
	# this is important since we'll be doing a bunch of divisions

	if boxes.dtype.kind=='i':
		boxes = boxes.astype('float')

	# initialize the list of picked indexes	
	pick = []


	#grab the coordinates of bounding boxes
	x1 = boxes[:,1]
	y1 = boxes[:,2]
	x2 = boxes[:,3]
	y2 = boxes[:,4]

	# compute the area of the bounding boxes and sort the bounding
	# boxes by the bottom-right y-coordinate of the bounding box
	area = (x2 - x1 + 1) * (y2 - y1 + 1)
	idxs = np.argsort(y2)

	#keep looping while some indexes still remain in indexes list
	while len(idxs)>0:

		#grab the last index and add the index value to the pick index list
		last = len(idxs)-1
		i = idxs[last]
		pick.append(i)

		# find the largest coordinate for start of bounding box
		xx1 = np.maximum(x1[i] ,x1[idxs[:last]])
		yy1 = np.maximum(y1[i] , y1[idxs[:last]])
		xx2 = np.maximum(x2[i] , x2[idxs[:last]])
		yy2 = np.maximum(y2[i] , y2[idxsp[:last]])

		# calculate width and height of bounding box
		w = np.maximum(0, xx2-xx1+1)
		h = np.maximum(0, yy2-yy1+1)

		#compute the ratio of overlap
		overlap = (w*h) / area[idxs[:last]]

		# delete all indexes from  the index that have 
		idxs = np.delete(idxs , np.concatenate(([last] , np.where(overlap>overlapthresh)[0])))

	return boxes[pick].astype('int')

