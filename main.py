#parking lot allotment

park2w={'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}

parkpc={'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}

parkcar={'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}

parkbus={'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}


while(1):

  ent_ext=input(' 1-Park in \n 2-take out vehicle from parking \n')

  p2wfull=1
  ppcfull=1
  pcarfull=1
  pbusfull=1
  typ=input('select the vehicle \n 1-two wheeler \n 2-Physically challenged \n 3-car \n 4-bus \n')
  if(ent_ext=='1'):
    
    #2 wheeler parking 
    if(typ=='1'):
      for i in park2w:
        if(park2w[i]==False):
          print('slot '+i+' is available')
          p2wfull=0;
          break
      if(p2wfull==0):
        print('park your vehicle at slot number '+i+'\n \n \n \n \n')
        park2w[i]=True 
      elif(p2wfull==1):
        print('2 Wheeler parking is full'+'\n \n \n \n \n')
  
    #physically challenged vehicle parking
    if(typ=='2'):
      for i in parkpc:
        if(parkpc[i]==False):
          print('slot '+i+' is available')
          ppcfull=0;
          break
      if(ppcfull==0):
        print('park your vehicle at slot number '+i+'\n \n \n \n \n')
        parkpc[i]=True 
      elif(ppcfull==1):
        print(' parking for Physically challenged is full'+'\n \n \n \n \n')


    #car parking
    if(typ=='3'):
      for i in parkcar:
        if(parkcar[i]==False):
          print('slot '+i+' is available')
          pcarfull=0;
          break
      if(pcarfull==0):
        print('park your vehicle at slot number '+i+'\n \n \n \n \n')
        parkcar[i]=True 
      elif(pcarfull==1):
        print(' car parking  is full'+'\n \n \n \n \n') 
      
      #bus parking
    if(typ=='4'):
      for i in parkbus:
        if(parkbus[i]==False):
          print('slot '+i+' is available')
          pbusfull=0;
          break
      if(pbusfull==0):
        print('park your vehicle at slot number '+i+'\n \n \n \n \n')
        parkbus[i]=True 
      elif(pbusfull==1):
        print(' bus parking is full'+'\n \n \n \n \n')
      
  
  #removing from parking

  if(ent_ext=='2'):
    
    #2 wheeler parking remove
    if(typ=='1'):
      i=input('enter the slot number \n')
      if(park2w[i]==True):
        print('please take your Vehicle from slot number '+i+'\n thank you for using the parking service'+'\n \n \n \n \n')
        park2w[i]=False
      
      else:
        print('no vehicle found on slot number '+i+'\n \n \n \n \n')

    #physically challenged parking removal
    if(typ=='2'):
      i=input('enter the slot number \n')
      if(parkpc[i]==True):
        print('please take your Vehicle from slot number '+i+'\n thank you for using the parking service'+'\n \n \n \n \n')
        parkpc[i]=False
      
      else:
        print('no vehicle found on slot number '+i+'\n \n \n \n \n')
    
    #car parking removal
    if(typ=='3'):
      i=input('enter the slot number \n')
      if(parkcar[i]==True):
        print('please take your Vehicle from slot number '+i+'\n thank you for using the parking service'+'\n \n \n \n \n')
        parkcar[i]=False
      
      else:
        print('no vehicle found on slot number '+i+'\n \n \n \n \n')

    #bus parking removal
    if(typ=='4'):
      i=input('enter the slot number \n')
      if(parkbus[i]==True):
        print('please take your Vehicle from slot number '+i+'\n thank you for using the parking service'+'\n \n \n \n \n')
        parkbus[i]=False
      
      else:
        print('no vehicle found on slot number '+i+'\n \n \n \n \n')


 




    