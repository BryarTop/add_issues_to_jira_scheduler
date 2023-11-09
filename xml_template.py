def make_header():
    return(f'\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n \
<TheSchedulerBackup xmlns="http://www.tt.com.pl">\n\
    <BackupInformation>\n\
        <JiraVersion>8.20.19</JiraVersion>\n\
        <PluginVersion>6.5.8</PluginVersion>\n\
        <BackupVersion>2.0</BackupVersion>\n\
        <BackupCreator>Bryar.Topham</BackupCreator>\n\
        <BackupTime>Oct 6, 2023 12:01:59 PM</BackupTime>\n\
        <ExportType>selected</ExportType>\n\
        <SelectedProjects>12641</SelectedProjects>\n\
        <SkipDisabled>false</SkipDisabled>\n\
        <SkipInvalid>false</SkipInvalid>\n\
    </BackupInformation>\n\
    <TheSchedulerData>\n\
')


def make_footer():
 return(f'\
            <SharedSIElement>\n\
                <sharedToEveryone>false</sharedToEveryone>\n\
                <sharedToLead>false</sharedToLead>\n\
                <sharedGroups></sharedGroups>\n\
                <sharedUsers>stephanie.soules</sharedUsers>\n\
                <sharedRoles>Administrators</sharedRoles>\n\
            </SharedSIElement>\n\
            <createLinked>0</createLinked>\n\
            <issueLinkTypeId>10220</issueLinkTypeId>\n\
            <createAsSubtask>false</createAsSubtask>\n\
            <parentIssueId>0</parentIssueId>\n\
        </ScheduledIssueElement>\n\
    </TheSchedulerData>\n\
</TheSchedulerBackup>\n'
)

def make_scheduled_issue_info(sched_issue_name):
    return(f'\
      <ScheduledIssueElement>\n\
        <name>{sched_issue_name}</name>\n\
        <createdBy>JIRAUSER16847</createdBy>\n\
        <description></description>\n\
        <projectId>12641</projectId>\n\
        <issueType>3</issueType>\n\
        <disabled>flase</disabled>\n\
        <increasePriority>false</increasePriority>\n\
        <createWhenResolution>true</createWhenResolution>\n\
        <createWhenPriorityHasMaxValue>false</createWhenPriorityHasMaxValue>\n')

def make_interval(start_date, monthly_interval):
    return(f'\
        <TriggerElement>\n\
            <triggerType>INTERVAL</triggerType>\n\
            <timeZoneID>Amercia/Denver</timeZoneID>\n\
            <intervalType>MONTHLY</intervalType>\n\
            <intervalDivider>{monthly_interval}</intervalDivider>\n\
            <startDate>{start_date}</startDate>\n\
            <skipScheduledExecutionAfterManual>false</skipScheduledExecutionAfterManual>\n\
        </TriggerElement>')

def __make_interval_helper__(segment):
    segs = {'25893':1,'22322':1,'22323':3,'22324':6,'22325':6,'22326':6}
    return segs.get(str(segment))

def __field_element_helper__(name,class_name):
    return(f'\
        <FieldElement>\n\
            <fieldName>customfield_{name}</fieldName>\n\
            <fieldClassName>com.atlassian.jira.issue.fields.{class_name}</fieldClassName>\n\
        </FieldElement>\n')


def define_body_elements():
    identical_fields = ['16392','17443','17442','14096','17441',
        '17447','14653','17446','13443','17445','14651','13522','13444',
        '14726','13514','13517','16749','16803','13519','16386','14443',
        '18328','13430','16388','17439','13499','14028']
    
    system_field_names = [
      {'name':'description','value':'DescriptionSystemField'},
      {'name':'attachment','value':'AttachmentSystemField'},
      {'name':'summary', 'value':'SummarySystemField'},
      {'name':'reporter','value':'ReporterSystemField'},
      {'name':'duedate','value':'DueDateSystemField'}
    ]
    system_field_indeces = [6,19,21,26,31]
    body_element = []
    for i in identical_fields:
        body_element.append(__field_element_helper__(i,'ImmutableCustomField'))
    sys_field_idx = 0
    for idx in system_field_indeces:
        body_element.insert(idx,__field_element_helper__(
            system_field_names[sys_field_idx]['name'],
            system_field_names[sys_field_idx]['value'],
        ))
        sys_field_idx+=1

    return(''.join(body_element))

def __params_helper__(name, value):
    return(f'\
        <ParamElement>\n\
            <paramName>{name}</paramName>\n\
            <paramValue>{value}</paramValue>\n\
        </ParamElement>\n'
    )

def define_body_params(custom_award, description, 
                           pricing_mod, stp, pids, region, num_programs,
                           pa, administration, solicitation_included, 
                           logo_photo, segment, lang, summary, budget_used,
                           hold_files, case_num, allowable_budget,
                           spec_instruct, due_date,):
    #n:name v:value
    params = [
            {'n':'dueDateType',       'v':'DYNAMIC'},
            {'n':'customfield_16392', 'v': ''},
            {'n':'customfield_14096', 'v': str(custom_award)},
            {'n':'description',       'v': str(description)},
            {'n':'customfield_14653', 'v': str(pricing_mod)},
            {'n':'customfield_13443', 'v': str(stp)},
            {'n':'customfield_14651', 'v': str(pids)},
            {'n':'customfield_13522', 'v': str(region)},
            {'n':'customfield_13444', 'v': str(num_programs)},
            {'n':'customfield_14726', 'v': str(pa)},
            {'n':'customfield_13514', 'v': str(administration)},
            {'n':'customfield_16749', 'v': str(solicitation_included)},
            {'n':'customfield_13517', 'v': str(logo_photo)},
            {'n':'customfield_16803', 'v': str(segment)},
            {'n':'customfield_13519', 'v': str(lang)},
            {'n':'summary',           'v': str(summary)},
            {'n':'customfield_16386', 'v': str(budget_used)},
            {'n':'customfield_18328', 'v': str(hold_files)},
            {'n':'customfield_14443', 'v': str(case_num)},
            {'n':'reporter',          'v': 'JIRAUSER16847'},
            {'n':'customfield_16388', 'v': str(allowable_budget)},
            {'n':'customfield_13499', 'v': str(spec_instruct)},
            {'n':'customfield_14028', 'v': '16462'},
            {'n':'duedate',           'v': ''},
            {'n':'dueDateValue',      'v': str(due_date)}
    ]
    return_obj = []
    for p in params:
        return_obj.append(__params_helper__(p['n'],p['v']))

    return ''.join(return_obj)


