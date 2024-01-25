import { ReactNode } from 'react';
import { Box, Drawer, List, ListItem, ListItemText, Toolbar } from '@mui/material';
import MyAppBar from '../components/navigation/appbar';

const Layout = ({ children }: { children: ReactNode }) => {
  return (
    <Box sx={{
      display:'flex'
    }}>
      <MyAppBar />
      <Box
        sx={{
          marginTop: {xs: 8, sm: 4},
          marginLeft: 3
        }}
      >
        {children}
      </Box>
    </Box>
  );
};

export default Layout;
