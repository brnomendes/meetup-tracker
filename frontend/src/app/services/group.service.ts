import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MeetupEvent, MeetupGroup } from '../models/meetup';

@Injectable({
  providedIn: 'root',
})
export class GroupService {
  url = `https://brnomendes-meetup-backend.herokuapp.com/groups`;

  constructor(private httpClient: HttpClient) {}

  getGroups(): Observable<MeetupGroup[]> {
    return this.httpClient.get<MeetupGroup[]>(this.url);
  }

  getEvents(groupId: number): Observable<MeetupEvent[]> {
    return this.httpClient.get<MeetupEvent[]>(`${this.url}/${groupId}/events/`);
  }

  updateGroup(groupId: number): Observable<string> {
    return this.httpClient.get<string>(`${this.url}/${groupId}/update/`);
  }
}
