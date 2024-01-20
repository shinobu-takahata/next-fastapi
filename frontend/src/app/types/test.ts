import { TestStatus } from "./testStatus";

export type Test = {
  id: number;
  name: string;
  status: TestStatus;
  description: string;
};
