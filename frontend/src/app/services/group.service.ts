import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MeetupGroup } from '../models/meetup';

@Injectable({
  providedIn: 'root',
})
export class GroupService {
  url = 'http://localhost:8000/groups/';

  constructor(private httpClient: HttpClient) {}

  getGroups(): Observable<MeetupGroup[]> {
    return this.httpClient.get<MeetupGroup[]>(this.url);
  }
}
