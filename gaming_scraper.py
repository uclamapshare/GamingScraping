

# function to add data
def add_data(target_container,data_class,data_index):
    raw_data = soupedrow.find_all('div',class_=data_class)[data_index].text
    clean_data = raw_data.strip()
    target_container.append(clean_data)
    return target_container

class Organization(object):
    def __init__(self,name):
        self.name = name
        
# loop through the results
#counter = 0
#for row in split_data:

#     Start grabbing from second row, as first row does not contain data
#    if counter > 1 and counter < len(split_data)-1:
#        soupedrow = BeautifulSoup(row,'html.parser')
#        add_data(DateReopened,'dateCol data',0)
#        add_data(DateClosed,'dateCol data',1)
#        add_data(Property,'orgCol data',0)
#        add_data(PropertyType,'statusCol data',0)
#        add_data(Status,'statusCol data',1)
#        add_data(Jurisdiction,'stateCol data',0)
#        add_data(Article,'articleCol data',0)
#    counter = counter + 1
