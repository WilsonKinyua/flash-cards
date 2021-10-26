import { Note } from './../classes/note';
import { Subject } from './../classes/subject';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ResponseDataService {
  constructor(private http: HttpClient) {}

  url = 'https://flash-cards-rest-api.herokuapp.com/api/';

  subject: Subject;
  notes: Note;

  // get all subjects
  getSubjects() {
    return this.http.get(this.url + 'subjects/');
  }
}
