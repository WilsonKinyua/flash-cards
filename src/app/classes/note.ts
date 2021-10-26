export class Note {
  constructor(
    public id: number,
    public user: number,
    public title: string,
    public description: string,
    public subject: string,
    public created_at: Date,
    public updated_at: Date
  ) {}
}
