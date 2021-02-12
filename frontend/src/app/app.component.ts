import {Component} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{

  // states of toggle selections, modelled as strings for easy DOM translation
  occasionSelection = '';
  navSelection = '';
  moodSelection = 'neutral';
  perspectiveSelection = 'one';
  modelSelection = '';

  // dynamic app states for transitions and loading animations
  initialState = true;
  loadingState = false;
  errorState = false;
  bertRetryState = false;
  rnnAddState = false;
  bertNoMoreOptions = false;

  // maximum number of suggestion fields
  maxSuggestions = 5;

  // occasion specific information
  weddingName1;
  weddingName2;
  birthdayName;
  birthdayAge;
  funeralName1;
  funeralName2;
  funeralGender = 'female';
  valentinesName;

  // output fields
  bertText = '';
  rnnSuggestions = [];
  acceptedRnnText = '';
  outputText = '';

  // inject http service
  constructor(private http: HttpClient) {
  }

  // -----------------------------------------------------------------------------------

  // Button Event handlers, individual functions to avoid passing DOM ids as parameters
  occasion_wedding() {
    this.occasionSelection = 'wedding';
    // set to recommended
    this.modelSelection = 'maidofhonor';
    this.occasion_shared();
  }

  occasion_birthday() {
    this.occasionSelection = 'birthday';
    // set to recommended
    this.modelSelection = 'shakespeare';
    this.occasion_shared();
  }

  occasion_funeral() {
    this.occasionSelection = 'funeral';
    // set to recommended
    this.modelSelection = 'shakespeare';
    this.occasion_shared();
  }

  occasion_valentine() {
    this.occasionSelection = 'valentines';
    // set to recommended
    this.modelSelection = 'michaeljackson';
    this.occasion_shared();

  }

  // shared procedure for all occasions
  occasion_shared(){
    // collapse nav-menu
    this.navSelection = '';
    // show tutorial
    this.initialState = true;
    // scroll past navbar and title
    document.body.scrollTop = 400; // For Safari
    document.documentElement.scrollTop = 400; // For Chrome, Firefox, IE and Opera
    // reset previous states
    this.loadingState = false;
    this.errorState = false;
    this.bertRetryState = false;
    this.rnnAddState = false;
    // reset output field
    this.bertText = '';
    this.acceptedRnnText = '';
    this.updateOutput();
  }

  // -----------------------------------------------------------------------------------

  // toggles for nav-menu elements
  nav_help() {
    if (this.navSelection === 'help') {
      this.navSelection = '';
    } else {
      this.navSelection = 'help';
    }
  }

  nav_how() {
    if (this.navSelection === 'how') {
      this.navSelection = '';
    } else {
      this.navSelection = 'how';
    }
  }

  nav_about() {
    if (this.navSelection === 'about') {
      this.navSelection = '';
    } else {
      this.navSelection = 'about';
    }
  }

  // -----------------------------------------------------------------------------------

  // call to action button when switching to new occasion
  generate() {
    // reset suggestions
    this.rnnSuggestions = [];
    // scroll to bottom
    document.body.scrollTop = 2000; // For Safari
    document.documentElement.scrollTop = 2000; // For Chrome, Firefox, IE and Opera
    // loading screen
    this.initialState = false;
    // generate bert part
    this.bertCall();
    // get 3 suggestions to start with
    this.rnnCall();
    this.rnnCall();
    this.rnnCall();
  }

  rnnCall() {
    // loading animation
    this.errorState = false;
    this.rnnAddState = true;

    // special parameters used for maidofhonor
    let params = new HttpParams();
    if (this.weddingName1 && this.occasionSelection === 'wedding'){
      params = params.set('name1', this.weddingName1);
    }
    if (this.weddingName2 && this.occasionSelection === 'wedding'){
      params = params.set('name2', this.weddingName2);
    }
    // http request and response callback
    this.http.get('http://localhost:5000/' + 'rnn_' + this.modelSelection, {params}).subscribe(
      // success
      data => {
        this.rnnSuggestions.push(data['text']);
        this.rnnAddState = false;
      },
      // error
      () => {
        this.rnnAddState = false;
        this.errorState = true;
      }
    );
  }

  bertCall() {
    // loading animation
    this.errorState = false;
    this.loadingState = true;
    this.bertNoMoreOptions = false;

    let endpoint = '';
    let params = new HttpParams();
    // shared parameters
    params = params.set('perspective', this.perspectiveSelection);
    params = params.set('mood', this.moodSelection);

    // optional occasion specific parameters, send if user has set them
    switch (this.occasionSelection) {
      case 'wedding':
        endpoint = 'bert_wedding';
        if (this.weddingName1 && this.weddingName1 !== '') {params = params.set('name1', this.weddingName1); }
        if (this.weddingName2 && this.weddingName2 !== '') {params = params.set('name2', this.weddingName2); }
        break;
      case 'birthday':
        endpoint = 'bert_birthday';
        if (this.birthdayName && this.birthdayName !== '') {params = params.set('name1', this.birthdayName); }
        if (this.birthdayAge && this.birthdayAge !== 0) {params = params.set('age', this.birthdayAge); }
        break;
      case 'funeral':
        endpoint = 'bert_funeral';
        if (this.funeralName1 && this.funeralName1 !== '') {params = params.set('name1', this.funeralName1); }
        if (this.funeralName2 && this.funeralName2 !== '') {params = params.set('name2', this.funeralName2); }
        if (this.funeralGender && this.funeralGender !== '') {params = params.set('gender', this.funeralGender); }
        break;
      case 'valentines':
        endpoint = 'bert_valentines';
        if (this.valentinesName && this.valentinesName !== '') {params = params.set('name1', this.valentinesName); }
        break;
      default:
    }

    // http request and response callback
    this.http.get('http://localhost:5000/' + endpoint, {params}).subscribe(
      // success
      data => {
        this.bertText = data['text'];
        this.updateOutput();
        this.loadingState = false;
      },
      // error
      () => {
        this.loadingState = false;
        this.errorState = true;
      }
    );

  }

  bertRetry() {
    // loading animation
    this.errorState = false;
    this.loadingState = false;
    this.bertRetryState = true;

    // http request and response callback
    this.http.get('http://localhost:5000/bert_retry', ).subscribe(
      // success
      data => {
        this.bertText = data['text'];
        this.updateOutput();
        // only show button if dictionaries are not empty yet
        this.bertNoMoreOptions = (data['warn'] === 'EMPTY');
        this.bertRetryState = false;
      },
      // error
      () => {
        this.bertRetryState = false;
        this.errorState = true;
      }
    );
  }

  // -----------------------------------------------------------------------------------

  // add suggestion to output field
  accept(i) {
    const selected = this.rnnSuggestions.splice(i, 1);
    this.acceptedRnnText = this.acceptedRnnText + '\n' + selected;
    this.updateOutput();
  }

  // remove suggestion
  decline(i) {
    this.rnnSuggestions.splice(i, 1);
  }

  // update output field
  updateOutput(){
    // bert and rnn parts are stored independently
    let text = this.bertText + this.acceptedRnnText;
    // title-case sentence beginnings
    const lines = text.split('\n');
    lines.forEach((line, index) => {
      lines[index] = line.charAt(0).toUpperCase() + line.slice(1);
    });
    text = lines.join('\n');
    this.outputText = text;

  }



}
