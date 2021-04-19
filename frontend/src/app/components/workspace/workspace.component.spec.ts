import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgxSpinnerModule } from 'ngx-spinner';
import { MessageService } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { DataViewModule } from 'primeng/dataview';
import { DialogModule } from 'primeng/dialog';
import { MenubarModule } from 'primeng/menubar';
import { ScrollPanelModule } from 'primeng/scrollpanel';
import { SidebarModule } from 'primeng/sidebar';
import { TagModule } from 'primeng/tag';
import { TimelineModule } from 'primeng/timeline';
import { ToastModule } from 'primeng/toast';
import { TooltipModule } from 'primeng/tooltip';
import { Observable, of } from 'rxjs';
import { MeetupEvent, MeetupGroup } from 'src/app/models/meetup';
import { GroupService } from 'src/app/services/group.service';

import { EventsComponent } from '../events/events.component';
import { GroupComponent } from '../group/group.component';
import { WorkspaceComponent } from './workspace.component';

class GroupServiceMock {
  getGroups(): Observable<MeetupGroup[]> {
    return of([
      { name: 'Group 1' } as MeetupGroup,
      { name: 'Group 2' } as MeetupGroup,
    ]);
  }

  getEvents(groupId: number): Observable<MeetupEvent[]> {
    return of([
      { name: 'Event 1' } as MeetupEvent,
      { name: 'Event 2' } as MeetupEvent,
    ]);
  }

  updateGroup(groupId: number): Observable<string> {
    return of('');
  }
}

describe('WorkspaceComponent', () => {
  let component: WorkspaceComponent;
  let fixture: ComponentFixture<WorkspaceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [WorkspaceComponent, GroupComponent, EventsComponent],
      providers: [
        MessageService,
        { provide: GroupService, useClass: GroupServiceMock },
      ],
      imports: [
        HttpClientTestingModule,
        CardModule,
        DataViewModule,
        ButtonModule,
        ScrollPanelModule,
        SidebarModule,
        BrowserAnimationsModule,
        MenubarModule,
        ToastModule,
        DialogModule,
        TimelineModule,
        TagModule,
        NgxSpinnerModule,
        TooltipModule,
      ],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkspaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should get groups', () => {
    const group = { id: 1, name: 'Group 1' } as MeetupGroup;
    component.updateGroup(group);
    expect(component.groups.map((g) => g.name)).toEqual(['Group 1', 'Group 2']);
  });

  it('should get events', () => {
    expect(component.currentEvents).toEqual([]);
    expect(component.currentEventsGroup).toBeUndefined();

    const group = { id: 1, name: 'Group 1' } as MeetupGroup;
    component.showEvents(group);

    expect(component.currentEvents.map((e) => e.name)).toEqual([
      'Event 1',
      'Event 2',
    ]);
    expect(component.currentEventsGroup).toEqual(group);
  });
});
