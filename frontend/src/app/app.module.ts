import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GroupService } from './services/group.service';
import { WorkspaceComponent } from './components/workspace/workspace.component';
import { GroupComponent } from './components/group/group.component';
import { EventsComponent } from './components/events/events.component';
import { CardModule } from 'primeng/card';
import { DataViewModule } from 'primeng/dataview';
import { ButtonModule } from 'primeng/button';
import { ScrollPanelModule } from 'primeng/scrollpanel';
import { SidebarModule } from 'primeng/sidebar';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MenubarModule } from 'primeng/menubar';
import { ToastModule } from 'primeng/toast';
import { DialogModule } from 'primeng/dialog';
import { TimelineModule } from 'primeng/timeline';
import { TagModule } from 'primeng/tag';
import { MessageService } from 'primeng/api';

@NgModule({
  declarations: [
    AppComponent,
    WorkspaceComponent,
    GroupComponent,
    EventsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
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
  ],
  providers: [GroupService, MessageService],
  bootstrap: [AppComponent],
})
export class AppModule {}
