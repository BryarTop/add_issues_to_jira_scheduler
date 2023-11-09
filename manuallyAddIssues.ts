import { WebDriver } from 'selenium-webdriver';

/*
	***************************************************************
	creating a class for this bitch
	***************************************************************
*/

class Issue {
	constructor(
		scheduledIssueName:string,
		summary:string,
		description:string,
		stp:string,
		pids:string,
		numProgs:string,
		segmentation:string,
		crmCaseNum:string,
		admin:string,
		holdFiles:string,
		dueDateAfterCreated:string,
		regionalTeam:string,
		logoPhoto:string,
		lang:string,
		custom:string,
		pa:string,
		budgetInConfig:string,
		solicitation:string,
		allowableBudget:string,
		pricingModel:string,
		specialInst:string,
		diffInst:string,
		firstExDate:string){
			this.scheduledIssueName = scheduledIssueName;
			this.summary = summary;
			this.description = description;
			this.stp = stp;
			this.pids = pids;
			this.numProgs = numProgs;
			this.segmentation = segmentation;
			this.crmCaseNum = crmCaseNum;
			this.admin = admin;
			this.holdFiles = holdFiles;
			this.dueDateAfterCreated = dueDateAfterCreated;
			this.regionalTeam = regionalTeam; 
			this.logoPhoto = logoPhoto;
			this.lang = lang;
			this.custom = custom;
			this.pa = pa;
			this.budgetInConfig = budgetInConfig;
			this.solicitation = solicitation;
			this.allowableBudget = allowableBudget;
			this.pricingModel = pricingModel;
			this.specialInst = specialInst;
			this.diffInst = diffInst;
			this.firstExDate = firstExDate;
	}
}

/*
	***************************************************************
	These are all of the helper functions. Each is called a handler. 
	***************************************************************
*/

const dueDateHandler = async (driver:WebDriver, dueAfterCreated:string) => {
	try {
		await driver.findElement(By.id('dueDateType-dynamic')).click();
		await driver.findElement(By.id('dueDate-dynamic')).sendKeys(dueAfterCreated);
	} catch(error){
		console.error(error);
	}
};

// cVonst dropDownHandler = (key:string,val:string) => {
// 	let dropdown, selected;
// 	dropdown = this.findElement(`#${key}`);
// 	dropdown.click();
//
// 	dropdown.findElements(By.tagname('option'))
// 		.then(function findMatchingOption(opts){
// 			opts.some(function(opt)
// 		})
// };

const textHandler = async (driver:WebDriver, key:string,val:string) => {
	try {
		await driver.findElement(By.Id(key)).sendKeys(val);
	} catch(e){
			return e
	}
};

const segHandler = (seg:string):number => {
	const interval:object = {
		'Signature':1,
		'Large Enterprise':1, 
		'Enterprise':3,
		'Coporate':6,
		'Mid':6,
		'Small':6,
	};
	return interval[seg];
};


/*
	***************************************************************
	These functions are the functions that should add values to their 
	respective pages. These rely on the handler functions
	***************************************************************
*/

const firstPage = async (driver:WebDriver, name:string) => {
	try {
		await driver.wait(until.urlContains('Step1!'));
		await driver.findElement(By.id('scheduledIssueName')).sendKeys(name);	
		await driver.findElement(By.id('select2-drop-mask')).sendKeys('Bryar.Topham')
		await driver.findElement(By.id('nextButton')).click();
	} catch (error) {
		return error
	} finally {
		return;
	}
};


const secondPage = async (driver:WebDriver, issue) => {
	type SelectorObject = {
		selector:string,
		val: string,
		fieldType:string
	}
	const opts:SelectorObject[] = [ //k: querySelector, v: value, ft:fieldType
		{selector:'summary',val: issue.summary,fieldType:'text'},
		{selector:'description-wiki-edit',val: issue.description, fieldType:'text'},
		{selector:'customField_13443',val: issue.stp, fieldType:'text'},
		{selector:'customfield_14651',val: issue.pids, fieldType:'text'},
		{selector:'customfield_13444',val: issue.numProgs, fieldType:'text'},
		{selector:'customfield_16803',val: issue.segmentation,fieldType:'dropdown'},
		{selector:'customfield_14443',val: issue.crmCaseNum,fieldType:'text'},
		{selector:'customfield_13514',val: issue.admin, fieldType:'dropdown'},
		{selector:'customfield_18328',val: issue.holdFiles, fieldType:'dropdown'},
		{selector:'customfield_14028',val: 'Spec', fieldType:'dropdown'},
		{selector:'customfield_13522',val: issue.regionalTeam, fieldType:'dropdown'},
		{selector:'customfield_13517',val: issue.logoPhoto, fieldType:'dropdown'},
		{selector:'customfield_13519',val: issue.lang, fieldType:'dropdown'},
		{selector:'customfield_14096',val: issue.custom, fieldType:'dropdown'},
		{selector:'customfield_14726',val: issue.pa, fieldType:'dropdown'},
		{selector:'customfield_16386',val: issue.budgetInConfig, fieldType:'dropdown'},
		{selector:'customfield_16749',val: issue.solicitation, fieldType:'dropdown'},
		{selector:'customfield_16388',val: issue.allowableBudget, fieldType:'dropdown'},
		{selector:'customfield_14653',val: issue.pricingModel, fieldType:'dropdown'},
		{selector:'customfield_13499',val: issue.specialInst, fieldType:'text'},
		{selector:'customfield_16391',val: issue.diffInst, fieldType:'text'},
	]
	try {
		opts.forEach(async(opt:SelectorObject) => {
			// await driver.findElement({id: opt.selector});
			let el:Element = await driver.findElement({id: opt.selector});
			await driver.wait(until.elementIsVisible(el),2000);
			await el.sendKeys(opt.val);
		})
		// await dueDateHandler(driver,issue.dueDateAfterCreated);
		document.querySelector('#nextButton').click();
	} catch (error) {
		return error
	}
};


const thirdPage = async (issue:Issue) => {
	try {
		await dropDownHandler('trigger-type','Interval');
		await dropDownHandler('interval-type','Monthly');
		textHandler('interval-divider',segHandler(issue.segmentation));
		document.querySelector('#addTriggerButton').click();
		document.querySelector('#nextButton').click();
	} catch (error) {
		return error
	}
};

const startRecurringSpec = async (driver:WebDriver) => {
	try {	
		// await driver.get('https://jira.octanner.com/projects/CAM?selectedItem=pl.com.tt.jira.plugin.theschedulerpro:scheduled-issues-project-tab-panel-link');
		await driver.executeScript(`document.querySelector('.css-mu6jxl').click()`);
		await driver.wait(until.urlContains('Step1!'));
	} finally {
		return;
	}
};

/*
	***************************************************************
	This is where the implementation of the selenium driver comes 
	into play. 
	***************************************************************
*/

import issues from './import_template.json';

const {Builder, By, Key, until} = require('selenium-webdriver');

let landingPage = 'https://jira.octanner.com/projects/CAM?selectedItem=pl.com.tt.jira.plugin.theschedulerpro:scheduled-issues-project-tab-panel-link';

const loginPageHandler = async (driver:WebDriver)=> {
	try{
		await	driver.get(landingPage);
		await driver.wait(until.urlContains('login'));
		await driver.wait(until.urlContains('project-tab-panel-link'));
	} finally {
		return ;
	}
};



const main = async (issues) => {
	let driver = new Builder().forBrowser('chrome').build();
	let count:number = 0;
	try {
		await loginPageHandler(driver);
		for(let i:number = 0; i<1; i++ ){
			const iss:Issue = Object.assign(new Issue, issues[i]);
			await startRecurringSpec(driver);
			await firstPage(driver,iss.scheduledIssueName);
			await secondPage(driver, iss);
		}
	} finally {
		// await driver.quit();
	}
};

await main(issues);
