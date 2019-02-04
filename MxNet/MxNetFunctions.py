import inspect
import os
import numpy as np
import mxnet as mx
from PIL import Image
from mxnet import gluon,nd
from mxnet.gluon.model_zoo import vision

# Add your model here
models=['VGG16','VGG19','CaffeNet','InceptionV3','NiN', 'ResidualNet152', 'ResNet101', 'SqueezeNet']



######## METHODS FOR LOAD MODELS ########

# Generic method to laod models from name
def loadModel(modelName):
    path=inspect.stack()[0][1]
    pos=path.rfind(os.sep)
    pathModel=path[:pos+1]+'Classification'+os.sep+'model'+os.sep+modelName+'.json'
    pathWeights=path[:pos+1]+'Classification'+os.sep+'weights'+os.sep+modelName+'.params'


    ctx = mx.gpu() if mx.test_utils.list_gpus() else mx.cpu()
    deserialized_net=gluon.nn.SymbolBlock.imports(pathModel, ['data'], pathWeights, ctx=ctx)

    return deserialized_net

def vgg16mxnetload():
    net= vision.vgg16(pretrained=True)
    net.hybridize()
    return net

def vgg19mxnetload():
    return loadModel('VGG19')

def caffenetmxnetload():
    return loadModel('CaffeNet')

def inceptionv3mxnetload():
    return loadModel('InceptionV3')

def ninmxnetload():
    return loadModel('NiN')

def residualnet152mxnetload():
    return loadModel('ResidualNet152')

def resnet101mxnetload():
    return loadModel('ResNet101')

def squeezenetmxnetload():
    return loadModel('SqueezeNet')


######## METHODS FOR PREPROCESS ########
def commonPreProcess(im):

    img=mx.image.image.imread(im)
    img=mx.image.image.imresize(img,224,224)
    # im=mx.image.image.imdecode(img)
    # print(img)
    # img=img.resize((224,224),Image.NEAREST)
    # image=img/255
    # img_arr=np.ndarray(img)
    # image=img_arr
    # print(image)

    # image =nd.transpose(im, (2,0,1))/255
    # image = mx.image.color_normalize(img,
    #                                   mean=mx.nd.array([0.485, 0.456, 0.406]),
    #                                   std=mx.nd.array([0.229, 0.224, 0.225]))

    img=mx.ndarray.swapaxes(img,0,2)

    img=mx.ndarray.cast(img, dtype='float32')
    return img

    # img=Image.open(im)
    # img=img.resize((224,224),Image.NEAREST)
    # img_arr=np.array(img.getdata()).astype(np.float32).reshape((img.size[0],img.size[1],3))
    # img_arr=np.swapaxes(img_arr,0,2)
    # img_arr=np.swapaxes(img_arr,1,2)
    # img_arr=img_arr[np.newaxis,:]
    #
    # return img_arr

def vgg16mxnetpreprocess(im):
    return commonPreProcess(im)

def vgg19mxnetpreprocess(im):
    return commonPreProcess(im)

def caffenetmxnetpreprocess(im):
    return commonPreProcess(im)

def inceptionv3mxnetpreprocess(im):
    return commonPreProcess(im)

def ninmxnetpreprocess(im):
    return commonPreProcess(im)

def residualnet152mxnetpreprocess(im):
    return commonPreProcess(im)

def resnet101mxnetpreprocess(im):
    return commonPreProcess(im)

def squeezenetmxnetpreprocess(im):
    return commonPreProcess(im)


######## METHODS FOR POSPROCESS ########
def commonPostProcess(result):
    result=np.squeeze(result)
    result=np.argsort(result)[::-1]
    path=inspect.stack()[0][1]
    pos=path.rfind(os.sep)
    path=path[:pos+1]
    labels=np.loadtxt(path+"synset_words.txt",str,delimiter='\n')
    return labels[result[0]]


def vgg16mxnetpostprocess(result):
    return commonPostProcess(result)

def vgg19mxnetpostprocess(result):
    return commonPostProcess(result)

def caffenetmxnetpostrocess(result):
    return commonPostProcess(result)

def inceptionv3mxnetpostprocess(result):
    return commonPostProcess(result)

def ninmxnetpostprocess(result):
    return commonPostProcess(result)

def residualnet152mxnetpostprocess(result):
    return commonPostProcess(result)

def resnet101mxnetpostprocess(result):
    return commonPostProcess(result)

def squeezenetmxnetpostprocess(result):
    return commonPostProcess(result)
