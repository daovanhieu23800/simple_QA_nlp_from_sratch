from dictionary import Dictionary
from dependency_parsing import DependencyParser
from word_segment import word_segmenting
query = "Máy bay nào đến thành phố Huế lúc 13:30HR ?. "
word_segment = word_segmenting(query)
dparset = DependencyParser(word_segment)
class GrammaticalRelation():
    def __init__(self,dependency_relation):
        self.dependency_relation = dependency_relation
        self.grammar_relation = []
       
    def convert_grammar_relation(self):
        relation_buffer = []
        for relation in self.dependency_relation:
            if 'WH_det' in relation:
                self.grammar_relation.append('WH_FLIGHT ?f')
            elif 'WHrun_time' in relation:
                self.grammar_relation.append('WH_RUN_TIME ?t')
            elif 'nsubj' in relation and "đến" in relation:
                self.grammar_relation.append('DEST_FLIGHT ?f')
            elif 'nmod' in relation:
                self.grammar_relation.append(f'FLIGHT (NAME flight_name ”{relation[-4:-1]}”)')
            else:
                relation_buffer.append(relation)
                if 'from_loc' in relation[0] and 'name_loc' in relation[1]:
                    self.grammar_relation.append(f'SOURCE (NAME city_source ”{relation[15:-1]}”)')

                if 'to_loc' in relation[0] and 'name_loc' in relation[1] or 'name' in relation[1]:
                    self.grammar_relation.append(f'DEST (NAME city_dest ”{relation[15:-1]}”)')
                
                if 'at_time(đến' in relation[0] and 'time' in relation[1]:
                    self.grammar_relation.append(f'AT_TIME( NAME at_time “{relation[12:-1]}”)')
                
        return self.grammar_relation


#print(dparset.get_result(),'123123123123123')
test = dparset.get_result()
print(GrammaticalRelation(test).convert_grammar_relation())