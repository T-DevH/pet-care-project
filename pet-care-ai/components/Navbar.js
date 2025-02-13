import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import Link from "next/link";

const Navbar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Pet Care AI
        </Typography>
        <Button color="inherit">
          <Link href="/">Home</Link>
        </Button>
        <Button color="inherit">
          <Link href="/chat">Chat</Link>
        </Button>
        <Button color="inherit">
          <Link href="/profile">Profile</Link>
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
